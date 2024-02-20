.. currentmodule:: discord

.. _guide_interactions_modals:

Modals
========

Modals are a form of interaction which prompt the user for additional information. They appear as a pop-up window and accept input using
components such as :class:`~discord.ui.TextInput`.

This section will detail how to create and use these modals in your code.


Defining a Modal
------------------

Modals share structural similarities with :ref:`Views <guide_interactions_views>`, both are used to design component-based UIs.

Modals are created by subclassing the :class:`~discord.ui.Modal` class.

For example:

.. code-block:: python

    class FeedbackForm(discord.ui.Modal, title='Feedback'):
        name = discord.ui.TextInput(label='Name')
        feedback = discord.ui.TextInput(label='Feedback', style=discord.TextStyle.long)
        additional_information = discord.ui.TextInput(
            label='Additional Information', style=discord.TextStyle.long, required=False
        )

        async def on_submit(self, interaction: discord.Interaction) -> None:
            ... # do something with the data

            await interaction.response.send_message(f'Thank you {self.name.value}, your submission was recorded.')

This produces a modal which appears on Discord as:

.. image:: /images/guide/interactions/modal_example.png

Let's break down the code:


Title
~~~~~~

When defining the class, a ``title`` keyword argument can be passed, which sets the default title of the modal.
Instances of the modal class can override this title by setting the ``title`` attribute or passing a ``title`` keyword argument to
the constructor. The title is required and is displayed at the top of the modal.


Fields
~~~~~~~

In our example above we have three class-attributes: ``name``, ``feedback``, and ``additional_information``, all of which are instances of the :class:`~discord.ui.TextInput` class.
In modal classes, class-attributes (which are instances of components) are used to represent the fields of the modal.

Discord requires modals contain between 1 and 5 fields.

.. note:: 

    Modal fields are displayed in the order in which they were defined. Our example from above defines ``name`` before it defines ``feedback``, 
    and that order is preserved when the ``FeedbackForm`` modal is displayed on Discord.

Fields can also be added to or removed from a modal instance using the :meth:`~discord.ui.Modal.add_item` and :meth:`~discord.ui.Modal.remove_item` methods.

.. warning:: 

    Ensure that class-attribute defined fields do not conflict with attributes or methods defined in the :class:`parent class <discord.ui.Modal>`, 
    as this will cause unexpected behaviour.


You can customize individual modal instances with normal attribute access and assignment.
For example, to change the label of the ``name`` field to ``'Your Name'`` you can do the following:

.. code-block:: python

    form = FeedbackForm()
    form.name.label = 'Your Name'


Handling User Responses
~~~~~~~~~~~~~~~~~~~~~~~~~

Once the user has clicked `Submit` the :meth:`Modal.on_submit <discord.ui.Modal.on_submit>` callback is called. 
The callback is passed a new :class:`~discord.Interaction` instance, which requires a response.

In the example above we respond by sending a message to the user confirming their submission was recorded.
Users responses to specific fields can be accessed via the field's ``value`` attribute.


Handling an error
~~~~~~~~~~~~~~~~~~

The :meth:`Modal.on_error <discord.ui.Modal.on_error>` method is called when an exception is raised
within :meth:`Modal.on_submit <discord.ui.Modal.on_submit>`, and can be used to handle an error or respond to the user.

This method is passed the exception raised, and the :class:`~discord.Interaction` instance, allowing you to handle the error and, 
if necessary, send a response to the user.


.. code-block:: python
    :emphasize-lines: 13-15

    class FeedbackForm(discord.ui.Modal, title='Feedback'):
        name = discord.ui.TextInput(label='Name')
        feedback = discord.ui.TextInput(label='Feedback', style=discord.TextStyle.long)
        additional_information = discord.ui.TextInput(
            label='Additional Information', style=discord.TextStyle.long, required=False
        )

        async def on_submit(self, interaction: discord.Interaction) -> None:
            ... # do something with the data

            await interaction.response.send_message(f'Thank you {self.name.value}, your submission was recorded.')

        async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
            if not interaction.response.is_done():
                await interaction.response.send_message('An error occurred, please try again.')


Sending a Modal
-----------------

A modal can be sent by calling the :meth:`InteractionResponse.send_modal` method when handling an :class:`Interaction`.

For example, you can respond with a modal when somebody uses a slash command:


.. code-block:: python

    @app_commands.command()
    async def feedback(interaction: discord.Interaction) -> None:
        """Send important feedback."""
        await interaction.response.send_modal(FeedbackForm())


Once a modal is sent, a user has the option to submit values. These should be handled either in an implementation of the
:meth:`~discord.ui.Modal.on_submit` method or via :meth:`Modal.wait() <discord.ui.Modal.wait>`,
in a similar fashion to the :ref:`confirmation prompt View example <guide_interactions_views>`.

.. note::

    It is currently not possible to tell if a user has closed the modal prompt without submitting.
