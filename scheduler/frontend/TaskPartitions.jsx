import React, { Component } from 'react';

class TaskPartitions extends Component {
state = {
    title: "Do the dishes",
    day: "Monday",
    startTime: "12:45",
    endTime: "1:30",
    weight: "Priority = Medium",
    }
    render(){
        return(
            <div>
                <h3>{this.props.title/*this.state.title*/}</h3>
                <span className= "badge badge-info">{this.props.day/*this.state.day*/}</span>
                <span className= "badge badge-secondary"> {this.props.startTime/*this.state.startTime*/}</span> 
                <b>-</b>
                <span className= "badge <m-2> badge-secondary"> {this.props.endTime/*this.state.endTime*/}</span> 
                <span className= {this.getPriorityBadgeClasses()}>{this.props.weight/*this.state.weight*/}</span>
                <button onClick= {this.props.onRemove} className= "btn btn-primary btn-sm m-2">Completed</button>

            </div>
        );
    };

    getPriorityBadgeClasses(){
        let classes = "badge <m-4> badge-danger";
        // classes += this.weight == "Priority = High" ? "danger" : (this.weight === "Priority = Medium" ? "warning" : "success");
        return classes;
    }

}
 
export default TaskPartitions;