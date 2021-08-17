import React, {Component} from 'react';
import '../App.css'
import axios from "axios";
import ViewSamplesTable from "../components/viewSamplesTable";

class ViewSamples extends Component {
    constructor(props){
    super(props);
    this.state={
      allSamples:[],
      isLoaded:false
    }
  }

  componentDidMount(){
    const _this=this;
    axios.get('/view-samples')
    .then(function (response) {
      _this.setState({
        allSamples:response.data.Data,
        isLoaded:"All samples:"
      });
    })
    .catch(function (error) {
      _this.setState({
        isLoaded: "Fail to view all samples!"
      })
        console.log(error);
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
                        <h5 className="card-title">{this.state.isLoaded}</h5>
                        <table className="table table-warning table-striped text-dark">
                            <thead>
                            <tr>
                                <th className="text-center">Type</th>
                                <th className="text-center">ID</th>
                                <th className="text-center">Location</th>
                                <th className="text-center">Current quantity</th>
                                <th className="text-center">Unit</th>
                                <th className="text-center">Current Status</th>
                                <th className="text-center">Current custodian</th>
                            </tr>
                            </thead>

                            <tbody>
                            <ViewSamplesTable allSamples={this.state.allSamples}/>
                            </tbody>
                        </table>

                    </div>
                    </body>
                </div>
            );
        }
  }
}

export default ViewSamples;
