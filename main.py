from flask import Flask, request, jsonify
from math import log
import re

app = Flask(__name__)


def parse_code_into_blocks(code):
    """
    Parses the submitted code into functional blocks based on Python's scoping rules.
    Modify this function to suit different programming languages or more complex parsing needs.
    """
    blocks = re.split(r'\n\s*\n|\n\s*def ', code)
    return [block.strip() for block in blocks if block.strip()]


def calculate_complexity(code_blocks):
    """
    Calculates a simple complexity based on the number of lines in each code block.
    """
    return sum(len(block.split('\n')) for block in code_blocks)


def enhanced_fractal_dimension(code_blocks):
    """
    Enhanced fractal dimension calculation using a box-counting method for code analysis.
    """
    scales = [1, 2, 4, 8, 16]
    counts = []
    for scale in scales:
        covered = set()
        count = 0
        for i in range(0, len(code_blocks), scale):
            for j in range(i, min(i + scale, len(code_blocks))):
                if code_blocks[j] not in covered:
                    count += 1
                    covered.add(code_blocks[j])
        counts.append(count)

    dimensions = [log(counts[i - 1] / counts[i]) / log(scales[i - 1] / scales[i]) for i in range(1, len(scales))]
    return sum(dimensions) / len(dimensions) if dimensions else 0


def dynamic_scaling_factor(code_blocks):
    """
    Applies dynamic scaling based on the number of code blocks, representing the 'infinity' concept.
    """
    scale = len(code_blocks)
    return max(1, log(scale) / log(2))


def interdisciplinary_fractal_analysis(code_blocks):
    """
    Scores the code by examining keywords that hint at complex systems, similar to disciplines such as physics and
    economics.
    """
    scores = {'physics': 0, 'economics': 0, 'biology': 0}
    for block in code_blocks:
        if 'quantum' in block:
            scores['physics'] += 1
        if 'market' in block:
            scores['economics'] += 1
        if 'ecosystem' in block:
            scores['biology'] += 1

    total_blocks = len(code_blocks)
    return sum(scores.values()) / total_blocks if total_blocks else 0


def assess_vulnerabilities(code):
    """
    Integrates all metrics to assess vulnerabilities.
    """
    code_blocks = parse_code_into_blocks(code)
    complexity = calculate_complexity(code_blocks)
    fractal_dimension = enhanced_fractal_dimension(code_blocks)
    dynamic_scale = dynamic_scaling_factor(code_blocks)
    interdisciplinary_score = interdisciplinary_fractal_analysis(code_blocks)

    # Combining all the factors to calculate the final vulnerability score
    vulnerability_score = (complexity * fractal_dimension * dynamic_scale) / (1 + interdisciplinary_score)
    return vulnerability_score


@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json['code']
    vulnerability_score = assess_vulnerabilities(code)
    return jsonify({
        'vulnerability_score': vulnerability_score,
        'message': 'Higher scores indicate higher risk of vulnerabilities. Interdisciplinary analysis included.'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
