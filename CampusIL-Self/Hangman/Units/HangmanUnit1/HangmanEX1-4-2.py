#Hangman Unit 1

def stage0 ():
    print(r"""    
                x-------x

    """)

def stage1():
    print(r"""    
                x-------x
                |
                |
                |
                |       
                |

    """)

def stage2():
    print(r"""     
                x-------x
                |       |
                |       0
                |
                |
                |

   """)

def stage3():
    print(r"""     
                x-------x
                |       |
                |       0
                |       |
                |   
                |


    """)

def stage4():
    print(r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |
                |

    """)

def stage5():
    print(r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |      /
                |

    """)

def stage6():
    print(r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |      / \
                |

    """)


stage0()
stage1()
stage2()
stage3()
stage4()
stage5()
stage6()