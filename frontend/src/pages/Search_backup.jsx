import React, {Component} from 'react';
import '../App.css';
import axios from 'axios';

class Search extends Component {
    constructor(props){
        super(props)
        this.state = {
            searchType: "",
            searchID:"",
            searchLoc:"",
            searchStatus:"",
            searchQ:"",
            searchUnit:"",
            searchCustodian:"",
        }
        this.handleInput = this.handleInput.bind(this);
        this.onButtonClick = this.onButtonClick.bind(this);
    }

    async startSearch() {
        const _this = this;
        await axios.post('/search', {
            sample_type: _this.state.searchType,
                    sample_ID: _this.state.searchID,
                    loc: _this.state.searchLoc,
                    status: _this.state.searchStatus,
                    Q: _this.state.searchQ,
                    unit: _this.state.searchUnit,
                    custodian: _this.state.searchCustodian
                })
                    .then(await function (response) {
                        _this.setState({
                            outputData: response.data
                        })
                    })
                    .catch(function (error) {
                        console.log(error);
                    })
            }

    handleInput = (e) => {
        if (e.target.id === "searchSampleType"){
            this.setState({
                searchType: e.target.value
            })
        }
        if (e.target.id === "searchSampleID"){
            this.setState({
                searchID: e.target.value
            })
        }
        if (e.target.id === "searchLocation"){
            this.setState({
                searchLoc: e.target.value
            })
        }
        if (e.target.id === "searchStatus"){
            this.setState({
                searchStatus: e.target.value
            })
        }
        if (e.target.id === "searchQuantity"){
            this.setState({
                searchQ: e.target.value
            })
        }
        if (e.target.id === "searchUnit"){
            this.setState({
                searchUnit: e.target.value
            })
        }
        if (e.target.id === "searchCustodian"){
            this.setState({
                searchCustodian: e.target.value
            })
        }

    }

    onButtonClick = (e) => {
        //console.log('.....');
        if (e.target.id === "searchButton") {
            return this.startSearch()
        }

        else if (e.target.id === "closeButton"){
            this.setState({
                searchType: "",
                searchID:"",
                searchLoc:"",
                searchStatus:"",
                searchQ:"",
                searchUnit:"",
                searchCustodian:"",
                outputData:""
            })
        }
    }

    render() {
        return (
        <div>
            <body className="d-flex text-left text-white bg-dark">
            <div className="main-page-config d-flex p-3 mx-auto flex-column">
                <h4 className="float-md-start font-monospace">Please log sample transaction：</h4>
                <form>
                    <div className="mb-0">
                        <label htmlFor="inputSampleType" className="Sample Type:">Sample Type:</label>
                        <input type="type" className="form-control" id="searchSampleType"
                               aria-describedby="typeHelp" onChange={this.handleInput}/>
                            <div id="typeHelp" className="form-text">e.g., blood, DNA, RNA, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputSampleID" className="form-label">Sample ID:</label>
                        <input type="id" className="form-control" id="searchSampleID"
                               aria-describedby="idHelp" onChange={this.handleInput}/>
                            <div id="idHelp" className="form-text">e.g., blo001, DNA123, RNA024, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="searchLocation" className="form-label">Storage Location:</label>
                        <input type="loc" className="form-control" id="searchLocation"
                               aria-describedby="locHelp" onChange={this.handleInput}/>
                            <div id="locHelp" className="form-text">e.g., f1, f5, f10, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="searchStatus" className="form-label">Status:</label>
                        <input type="status" className="form-control" id="searchStatus"
                               aria-describedby="statusHelp" onChange={this.handleInput}/>
                            <div id="statusHelp" className="form-text">i.e., available, in use, booked.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="searchQuantity" className="form-label">Quantity Variation:</label>
                        <input type="q" className="form-control" id="searchQuantity"
                               aria-describedby="qHelp" onChange={this.handleInput}/>
                            <div id="qHelp" className="form-text">e.g., 10, -5, -1.5, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="searchUnit" className="form-label">Unit:</label>
                        <input type="unit" className="form-control" id="searchUnit"
                               aria-describedby="unitHelp" onChange={this.handleInput}/>
                            <div id="unitHelp" className="form-text">e.g., ml, plate, tube, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="searchCustodian" className="form-label">Custodian:</label>
                        <input type="custodian" className="form-control" id="searchCustodian"
                               aria-describedby="custodianHelp" onChange={this.handleInput}/>
                            <div id="custodianHelp" className="form-text">e.g., peter, helen, mary, etc.</div>
                    </div>

                    <button type="button" className="btn btn-primary" data-bs-toggle="collapse"
                            data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample"
                            id= "searchButton" onClick={this.onButtonClick}>Search</button>

                    <div className="collapse" id="collapseExample">
                        <div>
                            <div className="card">
                                <div className="card-body">
                                    <p className="card-text">{JSON.stringify(this.state.outputData)}</p>
                                </div>
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

export default Search;



<div className="collapse" id="collapseExample">
                        <div>
                            <div className="card">
                                <div className="card-body text-dark">
                                    <h5 className="card-title">{this.state.isLoaded}</h5>
                                    {this.state.isLoaded === "Loaded" &&
                                    <button type="button" className="btn btn-primary">View</button>}
                                </div>
                            </div>
                        </div>
                    </div>
