import React, {Component} from 'react';
import '../App.css';
import axios from 'axios';

class Log extends Component {
    constructor(props){
        super(props)
        this.state = {
            inputType: "",
            inputID:"",
            inputLoc:"",
            inputStatus:"",
            inputQ:"",
            inputUnit:"",
            inputCustodian:"",
            outputData:""
        }
        this.handleInput = this.handleInput.bind(this);
        this.onButtonClick = this.onButtonClick.bind(this);
    }

    handleInput = (e) => {
        if (e.target.id === "inputSampleType"){
            this.setState({
                inputType: e.target.value
            })
        }

        if (e.target.id === "inputSampleID"){
            this.setState({
                inputID: e.target.value
            })
        }

        if (e.target.id === "inputLocation"){
            this.setState({
                inputLoc: e.target.value
            })
        }

        if (e.target.id === "inputStatus"){
            this.setState({
                inputStatus: e.target.value
            })
        }

        if (e.target.id === "inputQuantity"){
            this.setState({
                inputQ: e.target.value
            })
        }

        if (e.target.id === "inputUnit"){
            this.setState({
                inputUnit: e.target.value
            })
        }

        if (e.target.id === "inputCustodian"){
            this.setState({
                inputCustodian: e.target.value
            })
        }

    }

    onButtonClick = (e) => {
        if (e.target.id ==="submit"){

            const _this=this;    //先存一下this，以防使用箭头函数this会指向我们不希望它所指向的对象。
            axios.post('/log',{
                sample_type: _this.state.inputType,
                sample_ID: _this.state.inputID,
                loc: _this.state.inputLoc,
                status: _this.state.inputStatus,
                Q: _this.state.inputQ,
                unit: _this.state.inputUnit,
                custodian: _this.state.inputCustodian
            })
                .then(function (response) {
                    console.log(response);
                    _this.setState({
                        outputData: response.data
                    })
                })
                .catch(function (error) {
                    console.log(error);
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
                        <input type="type" className="form-control" id="inputSampleType"
                               aria-describedby="typeHelp" onChange={this.handleInput}/>
                            <div id="typeHelp" className="form-text">e.g., blood, DNA, RNA, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputSampleID" className="form-label">Sample ID:</label>
                        <input type="id" className="form-control" id="inputSampleID"
                               aria-describedby="idHelp" onChange={this.handleInput}/>
                            <div id="idHelp" className="form-text">e.g., blo001, DNA123, RNA024, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputLocation" className="form-label">Storage Location:</label>
                        <input type="loc" className="form-control" id="inputLocation"
                               aria-describedby="locHelp" onChange={this.handleInput}/>
                            <div id="locHelp" className="form-text">e.g., f1, f5, f10, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputStatus" className="form-label">Status:</label>
                        <input type="status" className="form-control" id="inputStatus"
                               aria-describedby="statusHelp" onChange={this.handleInput}/>
                            <div id="statusHelp" className="form-text">i.e., available, in use, booked.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputQuantity" className="form-label">Quantity Variation:</label>
                        <input type="q" className="form-control" id="inputQuantity"
                               aria-describedby="qHelp" onChange={this.handleInput}/>
                            <div id="qHelp" className="form-text">e.g., 10, -5, -1.5, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputUnit" className="form-label">Unit:</label>
                        <input type="unit" className="form-control" id="inputUnit"
                               aria-describedby="unitHelp" onChange={this.handleInput}/>
                            <div id="unitHelp" className="form-text">e.g., ml, plate, tube, etc.</div>
                    </div>
                    <div className="mb-1">
                        <label htmlFor="inputCustodian" className="form-label">Custodian:</label>
                        <input type="custodian" className="form-control" id="inputCustodian"
                               aria-describedby="custodianHelp" onChange={this.handleInput}/>
                            <div id="custodianHelp" className="form-text">e.g., peter, helen, mary, etc.</div>
                    </div>
                    <button type="submit" className="btn btn-primary" onClick={this.onButtonClick}>Submit</button>
                </form>

            </div>
            </body>
        </div>
    );
  }
}

export default Log;
