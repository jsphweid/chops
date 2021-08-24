import { Utils } from "../utils.ts";
import { Submission, Question, SuggestedQuestion } from "./types.ts";
import * as RawRequests from "./raw-requests/index.ts";
import { SubmitAnswerRequest } from "./raw-requests/submit-answer.ts";
import { Difficulty } from "../difficulty.ts";
import { Language } from "../language.ts";

export const getQuestionStartingCode = (
  question: Question.Type,
  language: Language.Type
): string => {
  const langSlug = Language.toLeetcodeSlugName(language);
  const found = question.codeSnippets.find((s) => s.langSlug === langSlug);
  if (!found) {
    return "Haven't fully implemented language " + langSlug;
  }
  return found.code;
};

export namespace LeetcodeService {
  export const getQuestionBySlug = (
    slug: string
  ): Promise<Question.Type | null> => RawRequests.getQuestionBySlug(slug);

  const waitForSubmission = (
    submissionId: number | string
  ): Promise<Submission.Type> =>
    RawRequests.checkSubmission(submissionId).then((data) => {
      if (RawRequests.isSubmissionCheckPending(data)) {
        return Utils.timeout(1000).then(() => waitForSubmission(submissionId));
      } else if (RawRequests.isSubmissionCheckAccepted(data)) {
        return Submission.fromRaw(data);
      } else if (RawRequests.isSubmissionCheckRejected(data)) {
        return Submission.fromRaw(data);
      } else {
        console.error(data);
        throw new Error("Not expecting this condition.");
      }
    });

  export const submitAnswer = (
    request: SubmitAnswerRequest
  ): Promise<Submission.Type> =>
    RawRequests.submitAnswer(request).then((data) =>
      waitForSubmission(data.submission_id)
    );

  export const getSuggestedQuestions = (
    difficulty: Difficulty.Type
  ): Promise<SuggestedQuestion.Type[]> =>
    RawRequests.getSuggestedQuestions(Difficulty.toLeetcodeName(difficulty));
}
