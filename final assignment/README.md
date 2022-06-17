# Flood risk prevention for the IJssel river in Gelderland - Group 22

This file serves as a guide to the IJssel river area flood management model. Apart from the base model, several other files were included or modified to allow for open exploration of model uncertainties and directed search and robustness analysis of prospective policies. These new or modified files and their functions are outlined here.

## Group composition
Group 22 consists of the following members:
* Gerdus van der Laarse     | 5486211
* Maanav Jhatakia           | 5551307
* Nicolò Canal              | 5625580
* Pascal Kampert            | 5609461
* Peter Schmidt             | 5616611
* Vaibhavi Srivastava       | 5462762

## Package dependencies

The following packages are required to run the `.py` and `.ipynb` files in this notebook:
1. `ema_workbench` - Exploratory Modelling Workbench used to verify model behaviour and find optimised policies.
2. `SALib` - Used for global sensitivity analysis (with built-in `ema_workbench` functions).
3. `numpy`, `pandas`, `matplotlib` and other commonly used general scientific and mathematical libraries.
4. `seaborn` - Used for clean visualisations.
5. `platypus` - Used for MORDM

## 1. Final report
The document `Final_report_Group_22.pdf` accompanies this project and should be used in conjunction with the notebooks in this repository.

## 2. Open exploration

In the `Open exploration.ipynb` notebook, the first part of the modelling workflow, Open exploration, was done. This consists of the following analyses:
1. Scenario Discovery
a. Sample generation over uncertainty space
b. Aggregation of outputs (only for problem formulation 3)
c. Analysis using PRIM
2. Global Sensitivity Analysis
a. Sample generation over uncertainty and lever spaces respectively, using SOBOL
b. Feature scoring

## 3. Directed search

In the `Directed search.ipynb` notebook, the latter part of the modelling workflow, Directed Search, was done. This notebook contains both policy discovery and robustness analysis of the candidate policies. This consists of:
1. Import of libraries & Definition of model input and model
2. Optimization over lever space
3. Reduction of pareto set of candiate policies at hand criteria-extent distribution
4. Robustness analysis of candidate policies under deep uncertainty

## 4. Problem formulation

In order to ensure the model outputs aligned with Gelderland's goals, problem formulation 3 in `problem_formulations.py` was slightly modified to only consider outputs of those dike rings that are found within Gelderland's effective borders.

## 5. Results

Since many, time-consuming analyses were required for this project, the results of all simulations were saved as compressed files under the `results` folder. These results were named as descriptively and uniquely possible.
* 1 scenarios 256 policy PF3 SA lever.tar.gz    | For global sensitivity analysis of levers - SOBOL samples over lever space
* 4000 scenarios 1 policy PF1.tar.gz            | For scenario discovery (and PRIM) using problem formulation 1
* 4000 scenarios 1 policy PF3.tar.gz            | For scenario discovery (and PRIM) using problem formulation 3
* results_convergence_robustness_40000.csv      | For MOEA (policy search) and 40000 nfe's 
* results_under_uncertainties_costs.tar.gz      | For robustness analysis of policies under worst costs scenarios
* results_under_uncertainties_deaths.tar.gz     | For robustness analysis of policies under worst deaths scenarios
* scens_expected_costs.tar.gz                   | Scenarios where costs outcome is of interest (90th percentile)
* scens_expected_deaths.tar.gz                  | Scenarios where deaths outcome is of interest (90th percentile)