# Account Number and Prize Generator

My project is to build an application that generates a random number and letter that is then outputted to create a prize. The application uses 4 containers that each have a separate purpose, Service1 is the frontend and displays the webpage and the output of the calculation. Service 2&3 both generate a random variable, Service 2 a random number and Service 3 creates 6 random letters between A-Z, Service 4 then will combine the outputs of S2&3 to give a required output, then S4 passes to S1 with the information.

The application will be set-up using a variety of tools such as Docker, Jenkins, Flask, Python and SQL.

# Requirments

The requirements set for the project are below.
Note that these are a minimum set of requirements and can be added onto during the duration of the project.
The requirements of the project are as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

You should consider the concept of MVP (Minimum Viable Product) as you plan your project, complete all the requirements before you add extra functionality that is not specified above.

# Trello Board

![Trello Board](/images/trelloboard.jpg)

My trello board progression, with a link to the most recent version [here][trello-link]!

This shows you my backlog of tasks, what is currently being worked on and also what has been completed.

[trello-link]: https://trello.com/b/hPAOsmi6/account-number-and-prize-generator

# Development Pipleine

![Development Pipeline](link)

Here is a diagram displaying and showing you the process of application and the services used to get from point A to point B. The Code and Jenkins is written and installed on one VM (Virtual Machine), the VM is linked to GitHub where the code is pushed to and using a webhook is linked to Jenkins so that the code can be updated publicly. When the code from GitHub is pushed to Jenkins, this then tests and builds the program and is then pushed to DockerHub as well. The Code creates the containers on two separate VM's one Manager and one Worker and then this is then accessible to the user via the NGINX server which is also acting as a load balancer.
# Test Results

Text

# Risk Assessment

![Risk Assessment] (link)

Here is my risk assessments deatailing all the risks that have and will be encountered during this project.

# Refrences

- All my knowledge has been given to me from my teacher Dara Oladapo and Harry Volker :)
- All me teaching had been from https://qa-community.co.uk/~/_/learning
- For any HTML querys I used https://www.w3schools.com/html/default.asp
- For any of my python querys I used https://thepythonguru.com/ and https://www.w3schools.com/python/default.asp/