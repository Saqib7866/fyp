import axios from "axios";
import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from "./layout/Header";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "",
    };
  }
  handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:8000/api/tutorials")
      .then((res) => {
        console.log("res: ", res);
      })
      .catch((error) => {
        console.log("error: ", error.response);
      });
  };
  render() {
    return (
      <>
        <Header />

        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input
              type="text"
              value={this.state.message}
              onChange={(e) => this.setState({ message: e.target.value })}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
