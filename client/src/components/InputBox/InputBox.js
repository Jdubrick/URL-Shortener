import React from "react";
import "./InputBox.css";

const InputBox = ({ placeholderText, readOnly }) => {
  return readOnly === false ? (
    <input className="input-box" type="text" placeholder={placeholderText} />
  ) : (
    <input
      className="input-box"
      type="text"
      placeholder={placeholderText}
      readOnly
    />
  );
};

export default InputBox;
