import React, {Component} from 'react';

class searchTable extends Component{
    constructor(props){
    super(props);
  }
  render(){
    return (
      this.props.outputData.map((each,i)=>{
          return (
              <tr key={i} className="text-center">
                <td>{each.id}</td>
                <td>{each.type}</td>
                <td>{each.Qvar}</td>
                <td>{each.Qvar_unit}</td>
              </tr>
          )       
      })
    )
  }
}

export default searchTable



