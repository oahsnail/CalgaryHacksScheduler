import React, { Component } from 'react';
import TaskPartitions from './TaskPartitions';


class TaskList extends Component {
    state = { 
        tasks: [
            {id: 1, title: "Do dishes", day: "Monday", startTime: "8:30", endTime: "8:45", weight: "Priority = high"},
            {id: 2, title: "Mow lawn", day: "Tuesday", startTime: "8:45", endTime: "9:00", weight: "Priority = high"},
            {id: 3, title: "Physics homework", day: "Wednesday", endTime: "9:30", weight: "Priority = medium"},
            {id: 4, title: "Chemistry homework", day: "Thursday", startTime: "9:30", endTime: "9:45", weight: "Priority = medium"},
            {id: 5, title: "Hackathon", day: "Friday", startTime: "12:30", endTime: "12:45", weight: "Priority = low"}
        ]
     };
    render() {
        return ( 
            <div>
                { this.state.tasks.map(TaskPartitions => <TaskPartitions key= {TaskPartitions.id}/>)}
                {/* {this.state.tasks.map(TaskPartitions => 
                <TaskPartitions key={TaskPartitions.id}/>)} */}
            </div>
         );
    }
}
 
export default TaskList;