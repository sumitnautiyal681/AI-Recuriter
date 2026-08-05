import { useState } from "react";
import ResumeUpload from "./ResumeUpload";
import api from "../api/api";

function JobForm() {
    const [jobTitle, setJobTitle] = useState("");
    const [jobDescription, setJobDescription] = useState("");
    const [requiredSkills, setRequiredSkills] = useState("");
    const [preferredSkills, setPreferredSkills] = useState("");
    const [experience, setExperience] = useState("");
    const [files, setFiles] = useState([]);
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);

const handleEvaluate = async () => {

    if (
        !jobTitle.trim() ||
        !jobDescription.trim() ||
        !requiredSkills.trim() ||
        !experience.trim()
    ) {
        alert("Please fill all required fields.");
        return;
    }

    if (files.length === 0) {
        alert("Please upload at least one resume.");
        return;
    }
    const formData = new FormData();

    formData.append("jobTitle", jobTitle);
    formData.append("jobDescription", jobDescription);
    formData.append("requiredSkills", requiredSkills);
    formData.append("preferredSkills", preferredSkills);
    formData.append("experience", experience);

    files.forEach((file) => {
        formData.append("files", file);
    });
    setLoading(true);
    try {
        
        const response = await api.post("/evaluate", formData);

        setResults(response.data.candidates);
        setLoading(false);

    } catch (error) {
        setLoading(false);
        alert(error.response?.data?.detail || "Something went wrong");

    }
};
    return (

        <>
            <div className="form-group">
                <label>Job Title</label>

               <input
    type="text"
    placeholder="Data Engineer"
    value={jobTitle}
    onChange={(e) => setJobTitle(e.target.value)}
/>
            </div>

            <div className="form-group">
                <label>Job Description</label>

                <textarea
    rows="6"
    placeholder="Enter Job Description"
    value={jobDescription}
    onChange={(e) => setJobDescription(e.target.value)}
></textarea>
            </div>

            <div className="form-group">
                <label>Required Skills</label>

                <input
    type="text"
    placeholder="Python, Spark, SQL"
    value={requiredSkills}
    onChange={(e) => setRequiredSkills(e.target.value)}
/>
            </div>

            <div className="form-group">
                <label>Preferred Skills</label>

                <input
    type="text"
    placeholder="Azure, Databricks"
    value={preferredSkills}
    onChange={(e) => setPreferredSkills(e.target.value)}
/>
            </div>

            <div className="form-group">
                <label>Minimum Experience</label>

                <input
    type="number"
    placeholder="3"
    value={experience}
    onChange={(e) => setExperience(e.target.value)}
/>
            </div>

            <ResumeUpload setFiles={setFiles}/>

            <button
    onClick={handleEvaluate}
    disabled={loading}
>
    {loading ? "Evaluating Candidates..." : "Evaluate Candidates"}
</button>
            {results.length > 0 && (

    <div className="results">

        <h2>Evaluation Results</h2>

        <div className="table-wrapper">

            <table>

                <thead>

                    <tr>
                        <th>Name</th>
                        <th>Score</th>
                        <th>Recommendation</th>
                    </tr>

                </thead>

                <tbody>

                    {results.map((candidate, index) => (

                        <tr key={index}>

                            <td>{candidate.name}</td>

                            <td>{candidate.evaluation.score}%</td>

                            <td>

                                <div>

                                    {candidate.evaluation?.matchedSkills?.map((skill, index) => (

                                        <span
                                            key={index}
                                            className="chip"
                                        >
                                            {skill}
                                        </span>

                                    ))}

                                </div>

                                <div style={{ marginTop: "8px", fontWeight: "bold" }}>
                                    {candidate.evaluation.recommendation}
                                </div>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    </div>

)}

        </>
    );
}

export default JobForm;