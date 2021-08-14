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
            <h4>{searchData['type']}</h4>
            <h4>{searchData['id']}</h4>
            <h4>{searchData['Qvar']}</h4>
            <h4>{searchData['Qvar_unit']}</h4>
          </div>
      )

      })
    )
  }
}

export default searchTable



