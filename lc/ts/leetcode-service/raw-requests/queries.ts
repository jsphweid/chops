import { Difficulty } from "./get-suggested-questions.ts";

export const getQuestionQuery = (slug: string) => ({
  query: `
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        content
        isPaidOnly
        exampleTestcases
        codeSnippets {
          lang
          langSlug
          code
        }
        stats
        solution {
          id
          canSeeDetail
          paidOnly
          hasVideoSolution
          paidOnlyVideo
        }
        status
        sampleTestCase
        metaData
        envInfo
      }
    }
  `,
  variables: { titleSlug: slug },
});

export const getSuggestedQuestionsQuery = (difficulty: Difficulty) => ({
  query: `
    query problemsetQuestionList(
      $categorySlug: String
      $limit: Int
      $skip: Int
      $filters: QuestionListFilterInput
    ) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        total: totalNum
        questions: data {
          title
          titleSlug
          difficulty
        }
      }
    }
  `,
  variables: {
    categorySlug: "algorithms",
    skip: 0,
    limit: 5,
    filters: { difficulty: difficulty, status: "NOT_STARTED" },
  },
});
