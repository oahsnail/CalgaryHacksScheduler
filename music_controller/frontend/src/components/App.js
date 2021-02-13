import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
    constructor(props) {
        super(props);

    }

    render() {
        return <h1>hi my name is {this.props.name}</h1>;
    }
}

const appDiv = document.getElementById("app");

// rendering app component inside appdiv
// the kwarg here is called a "prop", note how we're calling it in the return statement of App.render()
render(<App name="babingesh" />, appDiv);  