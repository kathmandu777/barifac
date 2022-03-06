import {
  Evaluation,
  SubjectFactory,
  SubjectResponse,
  ReadableScoreResponse,
  ReadableEvaluation,
  ReadableScoreFactory,
} from '..';

export interface EvaluationResponse {
  uuid: string;
  subject: SubjectResponse;
  name: string;
  rate: number;
  type: string;
}

export interface ReadableEvaluationResponse {
  evaluation_uuid: string;
  evaluation_name: string;
  rate: number;
  scores: ReadableScoreResponse[];
}

export class EvaluationFactory {
  public static createFromResponse(res: EvaluationResponse) {
    return new Evaluation(
      res.uuid,
      SubjectFactory.createFromResponse(res.subject),
      res.name,
      res.rate,
      res.type,
    );
  }
}

export class ReadableEvaluationFactory {
  public static createFromResponse(res: ReadableEvaluationResponse) {
    const scores = res.scores.map(ReadableScoreFactory.createFromResponse);
    return new ReadableEvaluation(
      res.evaluation_uuid,
      res.evaluation_name,
      res.rate,
      scores,
    );
  }
}