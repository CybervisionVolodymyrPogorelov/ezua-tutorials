## Ray vLLM Example

##### This guide illustrates configuring Ray to serve a LLM with vLLM.

### Prerequisites:
* Ensure you have enabled GPU support for Ray (https://github.com/HPEEzmeral/ezua-tutorials/blob/feature/fy24-q3/Data-Science/Ray/Ray-GPU/README.md) as vLLM requiers GPU to run (https://vllm.readthedocs.io/en/latest/getting_started/installation.html)
* Checkout Ray-GPU example from tutorials on how to enable GPU support for Ray
* With GPU support configured, create a `pytorch-cuda` notebook environment in Kubeflow.
* Ray client and server versions must match. Typically, `ray --version` can be used to verify the installed version.
* Run below commands from the terminal to install vLLM in the Ray kernel 
    . conda activate ray
      Set proxy if required
    . export HTTP_PROXY=<> && export HTTPS_PROXY=<> && export https_proxy="<>" && export http_proxy="<>"
    . pip install vllm==0.5.1

* To ensure optimal performance, use dedicated directories containing only the essential files needed for that job submission as a working directory.
* Activate the Ray-specific Python kernel in your notebook environment.
* Once the above prerequisites are fullfiled, follow the steps mentioned in Application Deployment in Ray-Serve tutorial to serve the LLM model using vLLM