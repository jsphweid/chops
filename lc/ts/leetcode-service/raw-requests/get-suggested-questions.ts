import { client } from "./client.ts";
import { getSuggestedQuestionsQuery } from "./queries.ts";
import { Difficulty } from "../../difficulty.ts";

export interface SuggestedQuestion {
  questionId: string;
  title: string;
  titleSlug: string;
  difficulty: string;
  isPaidOnly: boolean;
}

export type Difficulty = "EASY" | "MEDIUM" | "HARD";

interface GetSuggestedQuestionsResponse {
  question: SuggestedQuestion;
}

export const getSuggestedQuestions = (
  difficulty: Difficulty
): Promise<SuggestedQuestion[]> =>
  client
    .post("/graphql", getSuggestedQuestionsQuery(difficulty, 10))
    .then((response) => response.data.data.problemsetQuestionList.questions);
