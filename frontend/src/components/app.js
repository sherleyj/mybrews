import React, { Component } from "react";
import { render } from "react-dom";
// https://www.valentinog.com/blog/drf/#Django_REST_with_React_Django_and_React_together

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/hops")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data: data,
            loaded: true
          };
        });
      });
  }

  render() {
    console.log("APP is here");
    return (
      <ul>
        {this.state.data.map(hop => {
          return (
            <li key={hop.id}>
              {hop.name} - {hop.alpha_acid}
            </li>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
// ReactDOM.render(<App />, document.getElementById('app'));