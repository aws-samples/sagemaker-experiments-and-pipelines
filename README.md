## SageMaker Experiments and SageMaker Pipelines

The code presented in this repository shows how you can leverage Amazon SageMaker Experiments during your experimentation phase to track your tests and keep them organized. And it shows how Amazon SageMaker Pipelines can further streamline the organization of your experiments.

### Pre-requisites

To follow along the accompanying notebooks, you will need the following:

* an AWS account with sufficient permissions,
* an Amazon SageMaker Studio domain with internet access, and
* a user account in the domain with access to the default Amazon SageMaker execution role.

For detailed instructions on how to create an Amazon SageMaker Studio domain, you can refer to [this guide](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/prerequisites/option2).

### How-To

First, clone this repository in SageMaker Studio. You can do that either via the IDE (Git -> Clone a Repository), or via the terminal (`git clone https://github.com/aws-samples/sagemaker-experiments-and-pipelines.git`).

To run the two notebooks, we recommend using the `Data Science` image on the `Python 3` kernel of the Amazon SageMaker Studio IDE, as most of dependencies, such as `pandas`, `numpy`, and `matplotlib` are already installed.

[The first notebook](./01-Experiments.ipynb) walks you through a simple Machine Learning use case, showing how to interact with the SageMaker Experiments APIs, and how to use some of the plotting functionalities of SageMaker Studio.

[The second notebook](./02-PipelineExperiments.ipynb) wraps the manual steps executed in the first notebook to provide a programmatic and repeatable way to execute its steps: the data preparation, the hyperparameter tuning, and model creation. It also shows how to configure the pipeline so its every run gets organized within SageMaker Experiments.

## License Summary

This sample code is made available under the MIT-0 license. See the LICENSE file.
