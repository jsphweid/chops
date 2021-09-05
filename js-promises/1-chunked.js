const lib = require("./lib");

function chunkList(list) {
  const chunkSize = 5;
  const chunks = [];
  let i = 0;
  while (i < list.length) {
    chunks.push(list.slice(i, i + chunkSize));
    i += chunkSize;
  }

  return chunks;
}

async function dealWithPromises(promiseContainers) {
  let results = [];
  for (const chunk of chunkList(promiseContainers)) {
    const promises = chunk.map((container) => container.activate());
    results = [...results, ...(await Promise.all(promises))];
  }
  return results;
}

lib.runTest(dealWithPromises);
