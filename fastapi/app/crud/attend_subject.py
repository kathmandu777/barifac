from typing import Optional

from app.core.exceptions import (
    NOT_FOUND_OBJ_MATCHING_UUID,
    SAME_OBJECT_ALREADY_EXISTS,
    ApiException,
)
from app.db.database import get_db_session
from sqlalchemy.orm import scoped_session

from ..models import AttendSubject, Subject, User
from .base import BaseCRUD
from .subject import SubjectCRUD
from .user import UserCRUD

db_session = get_db_session()


class AttendSubjectCRUD(BaseCRUD):
    def __init__(self, db_session: scoped_session):
        super().__init__(db_session, AttendSubject)

    def get_by_user_and_subject(
        self, user: User, subject: Subject
    ) -> Optional[AttendSubject]:
        return (
            self.get_query()
            .filter_by(
                user_uuid=user.uuid,
                subject_uuid=subject.uuid,
            )
            .first()
        )

    def create(self, data: dict = {}) -> AttendSubject:
        subject: Optional[Subject] = SubjectCRUD(db_session).get_by_uuid(
            data["subject_uuid"]
        )
        if not subject:
            raise ApiException(NOT_FOUND_OBJ_MATCHING_UUID(Subject))
        user: Optional[User] = UserCRUD(db_session).get_by_uuid(data["user_uuid"])
        if not user:
            raise ApiException(NOT_FOUND_OBJ_MATCHING_UUID(User))
        attend_subject = self.get_by_user_and_subject(user, subject)
        return attend_subject if attend_subject else super().create(data)

    def update(self, obj: AttendSubject, data: dict = {}) -> AttendSubject:
        subject: Subject = data["subject"]
        user: User = data["user"]
        attend_subject = self.get_by_user_and_subject(user, subject)
        if attend_subject and attend_subject.uuid != obj.uuid:
            raise ApiException(SAME_OBJECT_ALREADY_EXISTS)
        return super().update(obj, data)
