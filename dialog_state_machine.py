# -*- coding: utf-8 -*-
from transitions import Machine

from settings import logger


class DialogStateMach(object):
    """
        Simple example of dialog constructor using State Machine.
    """
    # Declare all state of dialog
    states = ['start', 'menu',
              'step_1.1', 'step_1.2', 'step_1.3',
              'step_2.1', 'step_2.2', 'step_2.3',
              'step_3.1', 'step_3.2', 'step_3.3',
              'end']

    def __init__(self, dialog_name):

        self.dialog_name = dialog_name

        # Initialize the state machine
        self.machine = Machine(model=self, states=DialogStateMach.states, initial='start',
                               after_state_change='save_state_to_db')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # Init dialog using start command.
        self.machine.add_transition(trigger='start_dialog', source='start', dest='menu',
                                    after='start_dialog_fun')

        # Go to the main menu from any state
        self.machine.add_transition(trigger='back_to_menu', source='*', dest='menu',
                                    before='finalize_current_state_fun')

        # ************************************************************************************
        # Go to the first branch of dialog step 1.1.
        self.machine.add_transition(trigger='go_step_1.1', source='menu', dest='step_1.1',
                                    after='go_branch1_step1_fun')

        # Go to the first branch of dialog step 1.2.
        self.machine.add_transition(trigger='go_step_1.2', source='step_1.1', dest='step_1.2',
                                    after='go_branch1_step2_fun')

        # Go to the first branch of dialog step 1.3.
        self.machine.add_transition(trigger='go_step_1.3', source='step_1.2', dest='step_1.3',
                                    after='go_branch1_step3_fun')

        # ************************************************************************************
        # Go to the second branch of dialog step 2.1.
        self.machine.add_transition(trigger='go_step_2.1', source='menu', dest='step_2.1',
                                    after='go_branch2_step1_fun')

        # Go to the second branch of dialog step 2.2.
        self.machine.add_transition(trigger='go_step_2.2', source='step_2.1', dest='step_2.2',
                                    after='go_branch2_step2_fun')

        # Go to the second branch of dialog step 2.3.
        self.machine.add_transition(trigger='go_step_2.3', source='step_2.2', dest='step_2.3',
                                    after='go_branch2_step3_fun')

        # ************************************************************************************
        # Go to the third branch of dialog step 3.1.
        self.machine.add_transition(trigger='go_step_3.1', source='menu', dest='step_3.1',
                                    after='go_branch3_step1_fun')

        # Go to the third branch of dialog step 3.2.
        self.machine.add_transition(trigger='go_step_3.2', source='step_3.1', dest='step_3.2',
                                    after='go_branch3_step2_fun')

        # Go to the third branch of dialog step 3.3.
        self.machine.add_transition(trigger='go_step_3.3', source='step_3.2', dest='step_3.3',
                                    after='go_branch3_step3_fun')

        # self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])

    def start_dialog_fun(self):
        """ Send start command into dialog """
        logger.debug('START DIALOG')

    def finalize_current_state_fun(self):
        """ Finalize current state job before trigger state """
        print('FINALIZE CURRENT STATE JOB')

    # ************************************************************************************

    def go_branch1_step1_fun(self):
        logger.debug("NOW YOU ARE ON STATE 1.1")

    def go_branch1_step2_fun(self):
        logger.debug("NOW YOU ARE ON STATE 1.2")

    def go_branch1_step3_fun(self):
        logger.debug("NOW YOU ARE ON STATE 1.3")

    # ************************************************************************************

    def go_branch2_step1_fun(self):
        logger.debug("NOW YOU ARE ON STATE 2.1")

    def go_branch2_step2_fun(self):
        logger.debug("NOW YOU ARE ON STATE 2.2")

    def go_branch2_step3_fun(self):
        logger.debug("NOW YOU ARE ON STATE 2.3")

    # ************************************************************************************

    def go_branch3_step1_fun(self):
        logger.debug("NOW YOU ARE ON STATE 3.1")

    def go_branch3_step2_fun(self):
        logger.debug("NOW YOU ARE ON STATE 3.2")

    def go_branch3_step3_fun(self):
        logger.debug("NOW YOU ARE ON STATE 3.3")

    # ************************************************************************************

    def save_state_to_db(self):
        logger.debug("Save every state into PostgreSQL or Redis\n")


def main():
    bot_dialog = DialogStateMach(dialog_name='Telegram_bot')
    logger.debug("CURRENT STATE: {0}".format(bot_dialog.state))
    bot_dialog.trigger('start_dialog')

    logger.debug("CURRENT STATE: {0}".format(bot_dialog.state))
    bot_dialog.trigger('go_step_1.1')

    logger.debug("CURRENT STATE: {0}".format(bot_dialog.state))


if __name__ == '__main__':
    main()
