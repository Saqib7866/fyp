import axios from "axios";
import React, { Component } from "react";
import { Container, Row, Col } from "reactstrap";
import ReactDOM from "react-dom";
import Header from "./layout/Header";
import background from "./img/bg2.jpg";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "",
      errors: [],
      results: [],
    };
  }
  handleSubmit = (e) => {
    e.preventDefault();

    this.urgencyCheck();
  };

  urgencyCheck = () => {
    this.setState({ errors: [] });

    if (!this.state.message) {
      this.setState({ errors: ["Please enter some message."] });
      return;
    }

    axios
      .post("http://localhost:8000/api/urgency", {
        message: this.state.message,
      })
      .then((res) => {
        let { results } = this.state;
        let result = res.data;
        result.type = "urgency";
        result.position = results.length + 1;

        results = [result, ...results];
        this.setState({ results });
      })
      .catch((error) => {
        console.log("error: ", error.response);
      });
  };

  sentimentCheck = () => {
    this.setState({ errors: [] });

    if (!this.state.message) {
      this.setState({ errors: ["Please enter some message."] });
      return;
    }

    axios
      .post("http://localhost:8000/api/sentiment", {
        message: this.state.message,
      })
      .then((res) => {
        let { results } = this.state;
        let result = res.data;
        result.type = "sentiment";
        result.position = results.length + 1;

        results = [result, ...results];
        this.setState({ results });
      })
      .catch((error) => {
        console.log("error: ", error.response);
      });
  };

  render() {
    return (
      <div
        style={{
          backgroundImage: `url(${background})`,
          backgroundSize: "cover",
          height: "100%",
          backgroundRepeat: "repeat",
        }}
      >
        <div className="vh-100">
          <div className="text-center h1 bg-primary text-white">FYP</div>
          <div className="text-center h2 bg-info text-white">
            Sentimental Analysis Within Urgency Tweets
          </div>
          <Container>
            <Row className="mt-5">
              <Col xs="4"></Col>
              <Col xs="6">
                <form onSubmit={this.handleSubmit}>
                  {this.state.errors.map((error, i) => (
                    <div className="alert alert-danger" role="alert" key={i}>
                      {error}
                    </div>
                  ))}
                  <div className="form-group">
                    <label>Text To Check:</label>
                    <input
                      type="text"
                      className="form-control"
                      value={this.state.message}
                      onChange={(e) =>
                        this.setState({ message: e.target.value })
                      }
                    />
                  </div>
                  <div className="">
                    <button
                      className="btn btn-outline-primary m-2"
                      type="button"
                      onClick={this.urgencyCheck}
                    >
                      Check Urgency
                    </button>
                    <button
                      className="btn btn-outline-primary m-2"
                      type="button"
                      onClick={this.sentimentCheck}
                    >
                      Check Sentiment
                    </button>
                  </div>
                </form>
              </Col>
            </Row>
            <Row>
              <Col xs="12">
                <table className="table table-striped table-hover">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Message</th>
                      <th scope="col">Prediction</th>
                      <th scope="col">Type</th>
                    </tr>
                  </thead>
                  <tbody>
                    {this.state.results.map((result, i) => (
                      <tr key={i}>
                        <th scope="row">{result.position}</th>
                        <td>{result.message}</td>
                        <td>{result.prediction}</td>
                        <td>{result.type}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </Col>
            </Row>
          </Container>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
