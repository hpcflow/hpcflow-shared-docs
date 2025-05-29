.. jinja:: first_ctx

Demo workflows
----------------
A good way to get started with {{ app_name }} is to run a built-in demo workflows.
This will also test your installation, configuration, and some of your environments.

Submit a workflow
~~~~~~~~~~~~~~~~~

{{ app_name }} comes with some demo workflows, which can be listed using

.. code-block:: console

    {{ app_module }} demo-workflow --list


We can run the following command to copy the in-built workflow file to the current directory
(note the final dot at the end),

.. code-block:: console
    
    {{ app_module }} demo-workflow copy <workflow_name.yaml> .

which we can then use to submit the workflow.

.. code-block:: console

    {{ app_module }} go <workflow_name.yaml>

This small workflow should complete in less than 30s.
Note that there is also a convenience shortcut for the demo workflows which combines
the copy-then-submit pattern we saw above:    

.. code-block:: console

    {{ app_module }} demo-workflow go <workflow_name.yaml>

However, in general workflows would first be created in a yaml file which is then submitted using 
``{{ app_module }} go WORKFLOW_FILE``.

Check the status of a workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After submitting a workflow, you can check whether it has run successfully using

.. code-block:: console
    
    {{ app_module }} show -f

For clarification of the output, a legend can be shown using 

.. code-block:: console

    {{ app_module }} show --legend


Cancel a workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you might want to cancel a workflow that is running. Use

.. code-block:: console
    
    {{ app_module }} cancel WORKFLOW_REF

where ``WORKFLOW_REF`` is either the path to the workflow directory, 
or the ID of the workflow displayed by ``{{ app_module }} show``.
