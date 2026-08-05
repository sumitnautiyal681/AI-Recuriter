function ResumeUpload({ setFiles }) {

    const handleChange = (e) => {
        setFiles(Array.from(e.target.files));
    };

    return (
        <div className="form-group">

            <label>Upload Resumes</label>

            <input
                type="file"
                multiple
                accept=".pdf,.docx"
                onChange={handleChange}
            />

        </div>
    );
}

export default ResumeUpload;