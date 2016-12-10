# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s proposta.artistica -t test_propostaartistica.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src proposta.artistica.testing.PROPOSTA_ARTISTICA_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_propostaartistica.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a PropostaArtistica
  Given a logged-in site administrator
    and an add propostaartistica form
   When I type 'My PropostaArtistica' into the title field
    and I submit the form
   Then a propostaartistica with the title 'My PropostaArtistica' has been created

Scenario: As a site administrator I can view a PropostaArtistica
  Given a logged-in site administrator
    and a propostaartistica 'My PropostaArtistica'
   When I go to the propostaartistica view
   Then I can see the propostaartistica title 'My PropostaArtistica'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add propostaartistica form
  Go To  ${PLONE_URL}/++add++PropostaArtistica

a propostaartistica 'My PropostaArtistica'
  Create content  type=PropostaArtistica  id=my-propostaartistica  title=My PropostaArtistica


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the propostaartistica view
  Go To  ${PLONE_URL}/my-propostaartistica
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a propostaartistica with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the propostaartistica title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
