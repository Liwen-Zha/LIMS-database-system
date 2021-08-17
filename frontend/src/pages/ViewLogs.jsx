import React, {Component} from 'react';
import '../App.css'
import axios from "axios";
import ViewLogsTable from "../components/viewLogsTable";

class ViewLogs extends Component {
    constructor(props){
    super(props);
    this.state={
      allLogs:[],
      isLoaded:false
    }
  }

  componentDidMount(){
    const _this=this;
    axios.get('/view-logs')
    .then(function (response) {
      _this.setState({
        allLogs:response.data.Data,
        isLoaded:true
      });
    })
    .catch(function (error) {
      console.log(error);
      _this.setState({
        isLoaded:false,
        error:error
      })
    })
  }

  render() {
        if(!this.state.isLoaded){
            return (
                <div>
                    <body className="d-flex text-center text-white bg-dark">
                    <div className="main-page-config d-flex p-3 mx-auto flex-column">
                        <h1>Loading...</h1>
                    </div>
                    </body>
                </div>
            );
        }
        else {
            return (
                <div>
                    <body className="d-flex text-center text-white bg-dark">
                    <div className="main-page-config d-flex p-3 mx-auto flex-column">
                        <table className="table table-success table-striped text-dark">
                            <thead>
                            <tr>
                                <th className="text-center">Type</th>
                                <th className="text-center">ID</th>
                                <th className="text-center">Location</th>
                                <th className="text-center">Quantity change</th>
                                <th className="text-center">Unit</th>
                                <th className="text-center">Current quantity</th>
                                <th className="text-center">Unit</th>
                                <th className="text-center">Status</th>
                                <th className="text-center">Time</th>
                                <th className="text-center">Operated by</th>
                            </tr>
                            </thead>

                            <tbody>
                            <ViewLogsTable allLogs={this.state.allLogs}/>
                            </tbody>
                        </table>
                    </div>
                    </body>
                </div>
            );
        }
  }
}

export default ViewLogs;
