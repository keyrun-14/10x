import "./styles.css";
import React from "react";

export default function App() {
  const [value, setValue] = React.useState("");
  function change(e) {
    setValue(e.target.value);
  }

  function validate(value) {
    let x = value;
    let arr = [];
    let count = 0;
    let flag = 1;
    if (x.length % 2 !== 0) {
      flag = 0;
    } else {
      for (let i = 0; i < x.length; i++) {
        //console.log(x[i]);
        if (x[i] === "(" || x[i] === "{" || x[i] === "[") {
          arr.push(x[i]);
          //console.log(arr);
        } else if (x[i] === ")" || x[i] === "}" || x[i] === "]") {
          if (arr.length === 0) {
            break;
          }
          let a = arr.pop();
          //console.log(a);
          if (
            ("(" === a && x[i] === ")") ||
            ("{" === a && x[i] === "}") ||
            ("[" === a && x[i] === "]")
          ) {
            //console.log(x[i], "kkkk");

            count = count + 1;
            continue;
          }
        }
      }
    }
    //console.log(count);
    if (count === x.length / 2) {
      flag = 1;
    } else {
      flag = 0;
    }
    if (flag === 1) {
      alert("string is true");
    } else {
      alert("string is false");
    }
  }

  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <input onChange={(e) => change(e)} type="text" value={value}></input>
      <button onClick={() => validate(value)}>validate</button>
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}
