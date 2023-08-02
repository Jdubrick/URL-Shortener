import React from "react";
import "./InputBox.css";

const InputBox = ({
  placeholderText,
  readOnly,
  updateFunction,
  inputValue,
}) => {
  return readOnly === false ? (
    <input
      className="input-box"
      type="text"
      placeholder={placeholderText}
      onChange={(e) => updateFunction(e)}
      value={inputValue}
    />
  ) : (
    <input
      className="input-box"
      type="text"
      placeholder={placeholderText}
      value={inputValue}
      readOnly
    />
  );
};

export default InputBox;
