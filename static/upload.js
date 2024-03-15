// upload.js - this is the JS used by the Flask app, loaded by the HTML template
const ID_OF_FILE_ELEMENT = "idFile" // there must be an input of type file in the HTML template
const VALUE_OF_THE_NAME_ATTRIBUTE_OF_THE_INPUT_FILE_ELEMENT_IN_THE_HTML = "post_file"

// if combining with Flask, Flask must respond the /upload route
const REQUEST_URL = "/upload"

function uploadFile() {
    var formData = new FormData();

    var fileInput = document.getElementById(ID_OF_FILE_ELEMENT);
    var b_check = fileInput!=null
    if (b_check){
        var file = fileInput.files[0];
        formData.append(
            VALUE_OF_THE_NAME_ATTRIBUTE_OF_THE_INPUT_FILE_ELEMENT_IN_THE_HTML, file // whoever receives this post must know that the file is encoded as in a param named "post_file"
        );

        var dict_request_options = {
            method: 'POST',
            body: formData,
        } // dict_request_options

        // the Promise object represents the eventual completion (or failure) of the asynchronous operation.
        // 3 possibles = pending, fulfilled, rejected
        the_promise = fetch(
            REQUEST_URL,
            dict_request_options
        )

        // "then" to handle the case where the promise is fulfilled
        // "catch" to handle the case where the promise is rejected
        // the sequential pattern is a must, to chain returns from a callback as inputs to another callback
        // also, remember the arrow notation for params => code
        // in arrow functions, if there is only 1 expression in the body, the result of that is implicitly returned

        // this is a solution to make sure that, in case of catch, the original response is available
        let saved_response = null

        the_promise.then(
            p_response =>
            {
                saved_response = p_response
                return p_response.json() // convert the response to JSON + explicit return
            }
        )
        .then(p_data => console.log(p_data)) // access and use the actual data
        .catch(
            p_error =>
            {
                if(saved_response){
                    console.log("saved_response:", saved_response)
                }
                console.error('Error:', p_error)
            }
        )
    }// if
}// uploadFile

// upload.js ends