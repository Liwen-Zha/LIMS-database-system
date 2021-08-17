import React, {Component} from 'react';

class SearchTable extends Component{

    render(){
        return (
          this.props.outputData.map((eachLine,i)=>{
          return (
              <tr key={i} className="text-center">
                <td>{eachLine.type}</td>
                <td>{eachLine.id}</td>
                <td>{eachLine.loc}</td>
                <td>{eachLine.Qvar}</td>
                <td>{eachLine.Qvar_unit}</td>
                <td>{eachLine.status}</td>
                <td>{eachLine.custodian}</td>
                <td>{eachLine.time}</td>
              </tr>
          )
      })

    )
  }
}

export default SearchTable
