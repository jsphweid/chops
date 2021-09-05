const lib = require("./lib");

MAX_SIMUL = 5;

function timeout(millis) {
  return new Promise((resolve) => {
    setTimeout(resolve, millis);
  });
}

async function dealWithPromises(promiseContainers) {
  let totalNumProcessingCurrently = 0;
  let i = 0;
  while (i < promiseContainers.length) {
    if (totalNumProcessingCurrently < MAX_SIMUL) {
      totalNumProcessingCurrently++;
      const container = promiseContainers[i];
      i++;
      container.activate().then(() => {
        totalNumProcessingCurrently--;
      });
    }

    await timeout(5);
  }
}

lib.runTest(dealWithPromises);
