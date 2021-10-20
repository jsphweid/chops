import { client, authHeaders } from "./client.ts";
import { Language } from "../../language.ts";

interface SubmitAnswerResponse {
  submission_id: number;
}

export interface SubmitAnswerRequest {
  slug: string;
  problemId: string;
  language: Language.Type;
  code: string;
}

export const submitAnswer = (
  request: SubmitAnswerRequest
): Promise<SubmitAnswerResponse> =>
  client
    .post(
      `problems/${request.slug}/submit/`,
      {
        lang: Language.toLeetcodeSlugName(request.language),
        question_id: request.problemId,
        typed_code: request.code,
      },
      {
        headers: {
          ...authHeaders,
          referer: `https://leetcode.com/problems/${request.slug}/submissions/`,
        },
      }
    )
    .then((response) => response.data)
    .catch((response) => {
      console.log("error response", response);
      return;
    });
