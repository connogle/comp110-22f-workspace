"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730556651"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point: Point) -> float:
        """Returns the distance between tow distince point objects."""
        distance: float = sqrt(((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassignes the objects location to address its movement."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
  
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"    
        if self.is_immune():
            return "plum"
        return "green"
 
    def contract_disease(self) -> None:
        """Transfers the INFECTED attribute to a cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Checks if a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        """Checks if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False
        
    def is_immune(self) -> bool:
        """Checks if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def contact_with(self, cell: Cell) -> None:
        """When two cells are making contact, does the disease spreading thingy."""
        if self.is_infected() and cell.is_vulnerable():
            cell.contract_disease()
        if cell.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE

    
class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immunized: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0 or immunized < 0 or immunized + infected > cells:
            raise ValueError()
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        i: int = 0
        for _ in range(infected):
            self.population[i].contract_disease()
            i += 1
        for _ in range(immunized):
            self.population[i].immunize()
            i += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if constants.MIN_X > cell.location.x or constants.MAX_X < cell.location.x:
            cell.direction.x *= -1.0
        if constants.MIN_Y > cell.location.y or constants.MAX_Y < cell.location.y:
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Checks if two modeled objects are making contact."""
        for i in range(len(self.population)):      
            focus_cell: Cell = self.population[i]
            for ind in range(i + 1, len(self.population)):
                if self.population[ind].location.distance(focus_cell.location) < constants.CELL_RADIUS:
                    self.population[ind].contact_with(focus_cell)