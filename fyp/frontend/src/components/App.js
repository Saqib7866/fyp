import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from "./layout/Header";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <>
        <Header />
      </>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
