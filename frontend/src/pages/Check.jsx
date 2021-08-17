import React, {Component} from 'react';
import '../App.css';
import axios from 'axios';
import CheckTable from "../components/checkTable";

class Check extends Component {
    constructor(props){
        super(props)
        this.state = {
            searchType: "",
            searchID:"",
            searchLoc:"",
            checkStatus:"",
            checkCustodian:"",

            isLoaded:"Checking..."
        }
        this.handleInput = this.handleInput.bind(this);
        this.onButtonClick = this.onButtonClick.bind(this);
    }

    handleInput = (e) => {
        if (e.target.id === "checkSampleType"){
            this.setState({
                searchType: e.target.value
            })
        }
        if (e.target.id === "checkSampleID"){
            this.setState({
                searchID: e.target.value
            })
        }
        if (e.target.id === "checkLocation"){
            this.setState({
                searchLoc: e.target.value
            })
        }
        if (e.target.id === "checkStatus"){
            this.setState({
                checkStatus: e.target.value
            })
        }
        if (e.target.id === "checkCustodian"){
            this.setState({
                checkCustodian: e.target.value
            })
        }
    }

    onButtonClick = (e) => {
        if (e.target.id === "checkButton") {
            const _this = this;
            axios.post('/check', {
                sample_type: _this.state.searchType,
                sample_ID: _this.state.searchID,
                loc: _this.state.searchLoc,
                status: _this.state.checkStatus,
                custodian: _this.state.checkCustodian
            })
            .then(function (response) {
                _this.setState({
                    outputData: response.data.Data,
                    isLoaded: "Checked results："
                })
                console.log(response)
            })
            .catch(function (error) {
                console.log(error);
            })
        }
        else if (e.target.id === "closeButton"){
            this.setState({
                isLoaded:"Checking...",
                outputData:[]
            })
        }
    }

    render() {
        return (
        <div>
            <body className="d-flex text-left text-white bg-dark">
            <div className="main-page-config d-flex p-3 mx-auto flex-column">
                <h4 className="float-md-start font-monospace">Please input check criteria：</h4>
                <form>
                    <div className="mb-0">
                        <label htmlFor="checkSampleType" className="Sample Type:">Sample Type:</label>
                        <input type="type" className="form-control" id="checkSampleType"
                               aria-describedby="typeHelp" onChange={this.handleInput}/>
                            <div id="typeHelp" className="form-text">e.g., blood, DNA, RNA, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="checkSampleID" className="form-label">Sample ID:</label>
                        <input type="id" className="form-control" id="checkSampleID"
                               aria-describedby="idHelp" onChange={this.handleInput}/>
                            <div id="idHelp" className="form-text">e.g., blo001, DNA123, RNA024, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="checkLocation" className="form-label">Storage Location:</label>
                        <input type="loc" className="form-control" id="checkLocation"
                               aria-describedby="locHelp" onChange={this.handleInput}/>
                            <div id="locHelp" className="form-text">e.g., f1, f5, f10, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="checkStatus" className="form-label">Status:</label>
                        <input type="status" className="form-control" id="checkStatus"
                               aria-describedby="statusHelp" onChange={this.handleInput}/>
                            <div id="statusHelp" className="form-text">i.e., available, in use, booked.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="checkCustodian" className="form-label">Custodian:</label>
                        <input type="custodian" className="form-control" id="checkCustodian"
                               aria-describedby="custodianHelp" onChange={this.handleInput}/>
                            <div id="custodianHelp" className="form-text">e.g., peter, helen, mary, etc.</div>
                    </div>

                    <button type="button" className="btn btn-primary" data-bs-toggle="collapse"
                            data-bs-target="#collapseExample" aria-controls="collapseExample"
                            id= "checkButton" onClick={this.onButtonClick}>Check</button>

                    <div className="collapse" id="collapseExample">
                        <div>
                            <div className="card text-center">
                                <div className="card-body text-dark">
                                    <h5 className="card-title">{this.state.isLoaded}</h5>
                                    {this.state.isLoaded === "Checked results：" &&
                                        <div class = "table-responsive">
                                        <table className="table table-bordered border-primary">
                                            <thead>
                                            <tr>
                                                <th className="text-center">Type</th>
                                                <th className="text-center">ID</th>
                                                <th className="text-center">Location</th>
                                                <th className="text-center">Current quantity</th>
                                                <th className="text-center">Unit</th>
                                                <th className="text-center">Current status</th>
                                                <th className="text-center">Current custodian</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            <CheckTable outputData={this.state.outputData}/>
                                            </tbody>
                                        </table>
                                        </div>}
                                </div>
                                <button type="reset" className="btn btn-primary" id="closeButton" data-bs-toggle="collapse"
                                        data-bs-target="#collapseExample" aria-controls="collapseExample"
                                        onClick={this.onButtonClick}>Close</button>
                            </div>
                        </div>
                    </div>


                </form>

            </div>
            </body>
        </div>
    );
  }
}

export default Check;



