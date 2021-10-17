import { Difficulty } from "./get-suggested-questions.ts";

export const getQuestionQuery = (slug: string) => ({
  query: `
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
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

export const getSuggestedQuestionsQuery = (
  difficulty: Difficulty,
  limit: number
) => ({
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
          isPaidOnly
        }
      }
    }
  `,
  variables: {
    categorySlug: "algorithms",
    skip: 0,
    limit: limit,
    filters: { difficulty: difficulty, status: "NOT_STARTED" },
  },
});

export const getTopDiscussionTitlesQuery = (questionId: string) => ({
  query: `
    query questionTopicsList($questionId: String!, $orderBy: TopicSortingOption, $skip: Int, $query: String, $first: Int!, $tags: [String!]) {
      questionTopicsList(questionId: $questionId, orderBy: $orderBy, skip: $skip, query: $query, first: $first, tags: $tags) {
        edges {
          node {
            title
          }
        }
      }
    }
  `,
  variables: {
    orderBy: "most_votes",
    query: "",
    skip: 0,
    first: 15,
    tags: [],
    questionId,
  },
});
