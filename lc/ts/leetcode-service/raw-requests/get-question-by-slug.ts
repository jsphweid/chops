import { client } from "./client.ts";
import { getQuestionQuery } from "./queries.ts";

export interface Question {
  difficulty: "Easy" | "Medium" | "Hard";
  questionId: string;
  title: string;
  titleSlug: string;
  content: string;
  isPaidOnly: boolean;
  exampleTestcases: string;
  codeSnippets: CodeSnippetsEntity[];
  stats: string;
  solution: Solution;
  status: string;
  sampleTestCase: string;
  metaData: string;
  envInfo: string;
}

interface GetQuestionBySlugResponse {
  question: Question;
}

interface CodeSnippetsEntity {
  lang: string;
  langSlug: string;
  code: string;
}

interface Solution {
  id: string;
  canSeeDetail: boolean;
  paidOnly: boolean;
  hasVideoSolution: boolean;
  paidOnlyVideo: boolean;
}

export const getQuestionBySlug = (slug: string): Promise<Question | null> =>
  client
    .post("/graphql", getQuestionQuery(slug))
    .then((response) => response.data.data.question || null)
    .catch(console.log);
