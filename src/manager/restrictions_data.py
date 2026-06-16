dependencies_event_type = {
    "item_type":{
        "undeterminated": [

        ],
        "maneuver": [

        ],
        "reparation": [
            "tool"
        ],
        "medic operation": [
            "medic",
            "life suport",
        ],
        "minig operation": [

        ],
        "work meeting": [

        ],
        "comercial operation": [

        ],
        "defencive operation": [
            "weapon"
        ]
    },
    "specialist":{
        "undeterminated": [

        ],
        "maneuver": [
            "pilot"
        ],
        "reparation": [
            "reparation specialist"
        ],
        "medic operation": [
            "medic",
        ],
        "minig operation": [
            "mining specialist",
            "mechanic",
            "first aid"
        ],
        "work meeting": [
            "bureaucrat",
        ],
        "comercial operation": [
            "bureaucrat"
        ],
        "defencive operation": [
            "first aid"
        ]
    },
    "status":{
        "undeterminated": [

        ],
        "maneuver": [
            "captain"
        ],
        "reparation": [

        ],
        "medic operation": [

        ],
        "minig operation": [

        ],
        "work meeting": [
            "corporation representative"
        ],
        "comercial operation": [
            "corporation representative"
        ],
        "defencive operation": [
            "soldier"
        ]
    }

}

exclusion_event_type = {
    "item_type":{
        "undeterminated": [

        ],
        "maneuver": [

        ],
        "reparation": [
            
        ],
        "medic operation": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard",
        ],
        "minig operation": [

        ],
        "work meeting": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard",
        ],
        "comercial operation": [

        ],
        "defencive operation": [
            
        ]
    },
    "specialist":{
        "undeterminated": [

        ],
        "maneuver": [
            
        ],
        "reparation": [
            
        ],
        "medic operation": [
            
        ],
        "minig operation": [
            
        ],
        "work meeting": [
            
        ],
        "comercial operation": [
            
        ],
        "defencive operation": [
            
        ]
    },
    "status":{
        "undeterminated": [

        ],
        "maneuver": [
            "passenger",
        ],
        "reparation": [
            "passenger",
        ],
        "medic operation": [

        ],
        "minig operation": [
            "passenger",
        ],
        "work meeting": [
            "passenger",
        ],
        "comercial operation": [
            
        ],
        "defencive operation": [
            "passenger",
            "crew member"
        ]
    }

}

dependencies_place_name = {
    "item_type":{
        "Control Bridge": [],
        "Crew Quarters": [],
        "Nuclear Reactor": [
            "radio-hazard protection"
        ],
        "Mining Bay": [
            "vacuum protection"
        ],
        "Cargo Bay": [
            "chemical hazard protection"
        ],
        "Laboratory": [
            "bio-hazard protection"
        ],
        "Services Room": [],
        "Data Center": [],
        "Ship Exterior": [
            "vacuum protection"
        ]        
    },
    "specialist":{
        "Control Bridge": [
            "communications specialist"
        ],
        "Crew Quarters": [],
        "Nuclear Reactor": [
            "electric engineer",
            "nuclear engineer"
        ],
        "Mining Bay": [
            "mining specialist",
            "mechanic"
        ],
        "Cargo Bay": [
            "bureaucrat"
        ],
        "Laboratory": [],
        "Services Room": [],
        "Data Center": [
            "software engineer"
        ],
        "Ship Exterior": []
    },
    "status":{
        "Control Bridge": [],
        "Crew Quarters": [],
        "Nuclear Reactor": [],
        "Mining Bay": [],
        "Cargo Bay": [],
        "Laboratory": [],
        "Services Room": [],
        "Data Center": [],
        "Ship Exterior": []
    },
    "event_type":{
        "Control Bridge": [],
        "Crew Quarters": [],
        "Nuclear Reactor": [],
        "Mining Bay": [],
        "Cargo Bay": [],
        "Laboratory": [],
        "Services Room": [],
        "Data Center": [],
        "Ship Exterior": []
    }
}

exclusion_place_name = {
    "item_type":{
        "Control Bridge": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard"
        ],
        "Crew Quarters": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard"
        ],
        "Nuclear Reactor": [
            "bio-hazard",
            "chemical hazard"
        ],
        "Mining Bay": [],
        "Cargo Bay": [],
        "Laboratory": [],
        "Services Room": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard"
        ],
        "Data Center": [
            "bio-hazard",
            "radio-hazard",
            "chemical hazard"
        ],
        "Ship Exterior": []        
    },
    "specialist":{
        "Control Bridge": [],
        "Crew Quarters": [],
        "Nuclear Reactor": [],
        "Mining Bay": [],
        "Cargo Bay": [],
        "Laboratory": [],
        "Services Room": [],
        "Data Center": [],
        "Ship Exterior": []
    },
    "status":{
        "Control Bridge": [
            "passenger"
        ],
        "Crew Quarters": [],
        "Nuclear Reactor": [
            "passenger"
        ],
        "Mining Bay": [
            "passenger"
        ],
        "Cargo Bay": [],
        "Laboratory": [
            "passenger"
        ],
        "Services Room": [],
        "Data Center": [
            "passenger"
        ],
        "Ship Exterior": [
            "passenger"
        ]
    },
    "event_type":{
        "Control Bridge": [
            "comercial operation",
            "minig operation"
        ],
        "Crew Quarters": [
            "comercial operation",
            "maneuver",
            "minig operation"
        ],
        "Nuclear Reactor": [
            "comercial operation",
            "maneuver",
            "minig operation"
        ],
        "Mining Bay": [
            "maneuver"
        ],
        "Cargo Bay": [
            "maneuver",
            "minig operation"
        ],
        "Laboratory": [
            "comercial operation",
            "maneuver",
            "minig operation"
        ],
        "Services Room": [
            "maneuver",
            "minig operation"
        ],
        "Data Center": [
            "comercial operation",
            "maneuver",
            "minig operation"
        ],
        "Ship Exterior": [
            "comercial operation",
            "work meeting",
            "maneuver"
        ]
    }
}

dependencies_item_type = {}

exclusion_item_type = {}
# example, if there are space suits, the amount of space suits 
# most be >= to the amount of people
dependencies_amount_of_people = {

}