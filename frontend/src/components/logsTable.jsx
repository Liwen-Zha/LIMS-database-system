import React, {Component} from 'react';

class LogsTable extends Component{

    render(){
        return (
          this.props.allLogs.map((eachLine,i)=>{
          return (
              <tr key={i} className="text-center">
                <td>{eachLine.type}</td>
                <td>{eachLine.id}</td>
                <td>{eachLine.loc}</td>
                <td>{eachLine.Qvar}</td>
                <td>{eachLine.Qvar_unit}</td>
                <td>{eachLine.Qnow}</td>
                <td>{eachLine.Qnow_unit}</td>
                <td>{eachLine.status}</td>
                <td>{eachLine.time}</td>
                <td>{eachLine.custodian}</td>
              </tr>
          )
      })

    )
  }
}

export default LogsTable
