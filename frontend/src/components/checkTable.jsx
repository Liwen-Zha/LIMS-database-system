import React, {Component} from 'react';

class CheckTable extends Component{

    render(){
        return (
          this.props.outputData.map((eachLine,i)=>{
          return (
              <tr key={i} className="text-center">
                <td>{eachLine.type}</td>
                <td>{eachLine.id}</td>
                <td>{eachLine.loc}</td>
                <td>{eachLine.Qnow}</td>
                <td>{eachLine.Qnow_unit}</td>
                <td>{eachLine.status}</td>
                <td>{eachLine.latest_custodian}</td>
              </tr>
          )
      })

    )
  }
}

export default CheckTable
