Feature: Scenario Outline

  Scenario Outline: Blenders
    Given I put "<thing>" in a blender
    Then it should transform into "<other thing>"
    Then Put params into step "success"

    Examples: Amphibians
      | thing         | other thing |
      | Red Tree Frog | mush        |
      | apples        | apple juice |

    Examples: Consumer Electronics
      | thing        | other thing |
      | iPhone       | toxic waste |
      | Galaxy Nexus | toxic waste |

  Scenario: Example1
    Given a sample text loaded into the object
     """
     some text here
     """
    When we activate the object

  @tag
  Scenario: Example2
    Given a set of specific users
      | name      | department  |
      | Barry     | Beer Cans   |
      | Pudey     | Silly Walks |
      | Two-Lumps | Silly Walks |