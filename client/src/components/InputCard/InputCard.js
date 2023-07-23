import React from "react";
import "./InputCard.css";
import InputBox from "../InputBox/InputBox";
import ConvertButton from "../ConvertButton/ConvertButton";

const InputCard = () => {
  return (
    <div className="input-card">
      <InputBox placeholderText={"Enter long URL here"} readOnly={false} />
      <InputBox placeholderText={"Copy short URL here"} readOnly={true} />
      <ConvertButton />
    </div>
  );
};

export default InputCard;
