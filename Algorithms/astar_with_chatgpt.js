//This Code is meant to be written and executed in the p5.js editor
let gridSize = 50;
let gridCellSize = 10;
let grid;
let impassablePoints = [];

let startPoint;
let endPoint;
let path;

let currentStep = 0;
let astarComplete = false;

function setup() {
    let canvas = createCanvas(gridSize * gridCellSize, gridSize * gridCellSize);
    if (!canvas) {
        // Unable to create canvas, open alternative window
        window.open('alternative_window.html');
        return;
    }
    generateGrid();
    initialize();
    frameRate(1); // Slow down the frame rate for better visualization
}

function draw() {
    if (!astarComplete) {
        if (currentStep < path.length) {
            let currentPoint = path[currentStep];
            grid[currentPoint.x][currentPoint.y] = 2; // Mark current point as explored
            currentStep++;
        } else {
            astarComplete = true;
        }
        drawGrid();
    }
}

class Node {
    constructor(parent = null, position = null) {
        this.parent = parent;
        this.position = position;
        this.g = 0;
        this.h = 0;
        this.f = 0;
    }
}

function astar(start, end) {
    let openList = [];
    let closedList = [];
    let startNode = new Node(null, start);
    let endNode = new Node(null, end);

    openList.push(startNode);

    while (openList.length > 0) {
        let currentNode = openList[0];
        let currentIndex = 0;

        for (let index = 1; index < openList.length; index++) {
            if (openList[index].f < currentNode.f) {
                currentNode = openList[index];
                currentIndex = index;
            }
        }

        openList.splice(currentIndex, 1);
        closedList.push(currentNode);

        if (currentNode.position.x === endNode.position.x && currentNode.position.y === endNode.position.y) {
            let path = [];
            let current = currentNode;
            while (current != null) {
                path.push(current.position);
                current = current.parent;
            }
            return path.reverse();
        }

        let children = [];
        for (let newPosition of [[0, -1], [0, 1], [-1, 0], [1, 0]]) { // Adjacent squares
            let nodePosition = {x: currentNode.position.x + newPosition[0], y: currentNode.position.y + newPosition[1]};

            if (nodePosition.x > (grid.length - 1) || nodePosition.x < 0 || nodePosition.y > (grid[0].length - 1) || nodePosition.y < 0)
                continue;

            if (grid[nodePosition.x][nodePosition.y] != 0)
                continue;

            let newNode = new Node(currentNode, nodePosition);
            children.push(newNode);
        }

        for (let child of children) {
            if (closedList.find(closedChild => closedChild.position.x === child.position.x && closedChild.position.y === child.position.y))
                continue;

            child.g = currentNode.g + 1;
            child.h = ((child.position.x - endNode.position.x) ** 2) + ((child.position.y - endNode.position.y) ** 2);
            child.f = child.g + child.h;

            if (openList.find(openNode => child.position.x === openNode.position.x && child.position.y === openNode.position.y && child.g > openNode.g))
                continue;

            openList.push(child);
        }
    }

    return [];
}

function createGrid(size, impassablePoints) {
    let grid = new Array(size).fill(null).map(() => new Array(size).fill(0));
    impassablePoints.forEach(point => {
        grid[point.x][point.y] = 1; // Marking impassable objects
    });
    return grid;
}

function generateGrid() {
    impassablePoints = [];
    for (let i = 0; i < gridSize * gridSize * 0.2; i++) { // Adding 20% of the total cells as impassable obstacles
        let x = Math.floor(random(gridSize));
        let y = Math.floor(random(gridSize));
        impassablePoints.push({x: x, y: y});
    }
    grid = createGrid(gridSize, impassablePoints);
}

function getRandomPosition(range, gridSize) {
    return {
        x: Math.floor(Math.random() * (range.max - range.min + 1) + range.min),
        y: Math.floor(Math.random() * gridSize)
    };
}

function initialize() {
    // Generate random start (A) and end (C) points
    startPoint = getRandomPosition({min: 0, max: 4}, gridSize); // A within first 5 x positions
    endPoint = getRandomPosition({min: gridSize - 5, max: gridSize - 1}, gridSize); // C within last 5 x positions

    console.log(`Start Point (A):`, startPoint);
    console.log(`End Point (C):`, endPoint);

    path = astar(startPoint, endPoint);
    console.log(`Path:`, path);
}

function drawGrid() {
    background(255);
    // Draw grid
    stroke(200);
    for (let x = 0; x <= width; x += gridCellSize) {
        line(x, 0, x, height);
    }
    for (let y = 0; y <= height; y += gridCellSize) {
        line(0, y, width, y);
    }

    // Draw points
    noStroke();
    // Draw point A (startPoint) as green square
    fill(0, 255, 0);
    rect(startPoint.x * gridCellSize, startPoint.y * gridCellSize, gridCellSize, gridCellSize);
    // Draw point B (impassablePoints) as black square
    impassablePoints.forEach(point => {
        fill(0);
        rect(point.x * gridCellSize, point.y * gridCellSize, gridCellSize, gridCellSize);
    });
    // Draw point C (endPoint) as red square
    fill(255, 0, 0);
    rect(endPoint.x * gridCellSize, endPoint.y * gridCellSize, gridCellSize, gridCellSize);
    // Draw path between point A and point C in yellow squares
    if (path.length > 0) {
        fill(255, 255, 0);
        path.forEach(point => {
            if (!(point.x === startPoint.x && point.y === startPoint.y) && !(point.x === endPoint.x && point.y === endPoint.y)) {
                rect(point.x * gridCellSize, point.y * gridCellSize, gridCellSize, gridCellSize);
            }
        });
    }
    // Draw explored squares during the A* search in light grey
    fill(200);
    for (let x = 0; x < gridSize; x++) {
        for (let y = 0; y < gridSize; y++) {
            if (grid[x][y] === 2 && !(x === startPoint.x && y === startPoint.y) && !(x === endPoint.x && y === endPoint.y)) {
                rect(x * gridCellSize, y * gridCellSize, gridCellSize, gridCellSize);
            }
        }
    }
}
