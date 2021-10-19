import { Difficulty } from "./get-suggested-problems.ts";

export const getProblemQuery = (slug: string) => ({
  query: `
    query problemData($titleSlug: String!) {
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

export const getSuggestedProblemsQuery = (
  difficulty: Difficulty,
  limit: number
) => ({
  query: `
    query problemsetProblemList(
      $categorySlug: String
      $limit: Int
      $skip: Int
      $filters: QuestionListFilterInput
    ) {
      problemsetProblemList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        total: totalNum
        problems: data {
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

export const getTopDiscussionTitlesQuery = (problemId: string) => ({
  query: `
    query problemTopicsList($problemId: String!, $orderBy: TopicSortingOption, $skip: Int, $query: String, $first: Int!, $tags: [String!]) {
      problemTopicsList(problemId: $problemId, orderBy: $orderBy, skip: $skip, query: $query, first: $first, tags: $tags) {
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
    problemId,
  },
});
