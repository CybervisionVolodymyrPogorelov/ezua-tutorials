## Ray Serve vLLM Example

##### This guide illustrates configuring Ray to serve a LLM with vLLM.

### Prerequisites:
* Ensure you have enabled GPU support for Ray (https://github.com/HPEEzmeral/ezua-tutorials/blob/feature/fy24-q3/Data-Science/Ray/Ray-GPU/README.md) as vLLM requiers GPU to run (https://vllm.readthedocs.io/en/latest/getting_started/installation.html)
* Checkout Ray-GPU example from tutorials on how to enable GPU support for Ray
* With GPU support configured, create a `jupyter-tensorflow-cuda-full` notebook environment in Kubeflow.
* Ray client and server versions must match. Typically, `ray --version` can be used to verify the installed version.
* Run below commands from the terminal to install vLLM in the Ray kernel 
    ``` pyton
    conda activate ray
    # Proxies are optional based on your env
    export HTTP_PROXY=<>
    export HTTPS_PROXY=<>
    export https_proxy=<>
    && export http_proxy=<>
    pip install vllm==0.5.1
    ```
* To ensure optimal performance, use dedicated directories containing only the essential files needed for that job submission as a working directory.
* Activate the Ray-specific Python kernel in your notebook environment.
* Once the above prerequisites are fulfilled, follow below the steps:

### Running vLLM with Ray Serve:

* Make sure that both `ray-serve-vllm-executor.ipynb` and `ray_serve_vllm_example.py` are present inside the same dedicated directory.
* `serve build` will generate deployment config file:

  ![1_building_serve_app.png](resources/1_building_serve_app.png)

* Modify the deployment config file after executing the workaround. Please note that you need to specify `working_dir` and `pip` installation as below. (Sample config file is provided under resources.)

  ![2_modifying_depoyment_config.png](resources/2_modifying_depoyment_config.png)

* Deploy the app after config file is ready:

  ![3_deploy_the_app.png](resources/3_deploy_the_app.png)

* TODO: Add screenshot of Ray Serve UI section as a check for deployment status

  ### TODO: Add screenshot here

* Once the deployment is ready, you can end request:

  ![5_send_request.png](resources/5_send_request.png)
