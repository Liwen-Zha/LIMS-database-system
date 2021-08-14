import React, {Component} from 'react';

class searchTable extends Component{n
  constructor(props){
    super(props);
  }
  render(){
    return (
      this.props.jsonData.map((searchData,i)=>{
      return (
          <div key={i} className="text-center">
            <h4>{JSON.stringify(searchData["type"])}</h4>
            <h4>{JSON.stringify(searchData["id"])}</h4>
            <h4>{JSON.stringify(searchData["Qvar"])}</h4>
            <h4>{JSON.stringify(searchData["Qvar_unit"])}</h4>
          </div>
      )

      })
    )
  }
}

export default searchTable



