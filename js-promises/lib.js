function genPromise() {
  let isPending = false;
  let isFulfilled = false;
  let isRejected = false;
  let isResolved = false;
  const _gen = () => {
    isPending = true;
    return new Promise((resolve) => {
      setTimeout(resolve, Math.random() * 1000);
    })
      .then((data) => {
        isPending = false;
        isResolved = true;
        isFulfilled = true;
        return data;
      })
      .catch((e) => {
        isPending = false;
        isRejected = true;
        isFulfilled = true;
        throw new Error(e);
      });
  };

  return {
    isPending: () => isPending,
    isFulfilled: () => isFulfilled,
    isRejected: () => isRejected,
    isResolved: () => isResolved,
    activate: _gen,
  };
}

function runTest(fn) {
  // takes in a fn that gets called with a bunch of promises
  const promises = Array.from({ length: 50 }).map(genPromise);

  fn(promises);

  setInterval(() => {
    const str = promises.reduce(
      (prev, curr) => `${prev}${curr.isPending() ? "p" : "|"}`,
      ""
    );
    console.log(str);
  }, 50);
}

module.exports = {
  runTest,
};
