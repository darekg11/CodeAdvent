const calculateCaptchaSum = captcha => {
  const array = [...captcha].map(stringNumber => Number(stringNumber));
  let captchaSum = 0;

  for (let capthaCnt = 0; capthaCnt < array.length - 1; capthaCnt += 1) {
    const element = array[capthaCnt];
    const nextElement = array[capthaCnt + 1];
    if (element === nextElement) {
      captchaSum += element;
    }
  }
  if (array.length > 0) {
    const lastElement = array[array.length - 1];
    if (lastElement === array[0]) {
      captchaSum += lastElement;
    }
  }
  return captchaSum;
};

const calculateCaptchaSumHalfwayAround = captcha => {
  const array = [...captcha].map(stringNumber => Number(stringNumber));
  let captchaSum = 0;
  const jumpGap = array.length / 2;

  for (let capthaCnt = 0; capthaCnt < array.length; capthaCnt += 1) {
    const element = array[capthaCnt];
    const nextJumpIndex = capthaCnt + jumpGap;
    const nextIndexValue =
      nextJumpIndex >= array.length
        ? array[nextJumpIndex - array.length]
        : array[nextJumpIndex];
    if (element === nextIndexValue) {
      captchaSum += element;
    }
  }
  return captchaSum;
};

exports.calculateCaptchaSum = calculateCaptchaSum;
exports.calculateCaptchaSumHalfwayAround = calculateCaptchaSumHalfwayAround;
