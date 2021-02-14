import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from './HomePage';
import TaskList from './TaskList'
import TaskPartitions from './TaskPartitions'


export default class App extends Component {
    constructor(props) {
        super(props);

    }

    render() {
        return (<div>
            <TaskPartitions></TaskPartitions>
            <h1>this page was made by {this.props.name} the wise</h1>
        </div>);



        // equivalently: return <HomePage/>; 
        // return 
    }
}

const appDiv = document.getElementById("app");

// rendering app component inside appdiv
// the kwarg here is called a "prop", note how we're calling it in the return statement of App.render()
render(<App name="babingesh" />, appDiv);  